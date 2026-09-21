/* ============================================================
   Kit común de las herramientas.
   Se inserta completo en cada archivo: no hay dependencias externas
   y todo funciona abriendo el HTML con doble clic, sin internet.
   ============================================================ */
var Kit = (function(){

  var CLAVE = "herramienta";
  var ganchos = {};            // extra, restaurar, alCambiar, resumen
  var listo = false;

  /* ---------- utilidades ---------- */
  function $(id){ return document.getElementById(id); }
  function crearEl(tag, clase, texto){
    var e = document.createElement(tag);
    if(clase) e.className = clase;
    if(texto !== undefined) e.textContent = texto;
    return e;
  }
  function svg(tag, attrs){
    var e = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for(var k in attrs) e.setAttribute(k, attrs[k]);
    return e;
  }
  /* mezcla dos colores hex; t=0 devuelve a, t=1 devuelve b */
  function mezcla(a, b, t){
    t = Math.max(0, Math.min(1, t));
    function n(c, i){ return parseInt(c.substr(1 + i*2, 2), 16); }
    var r = Math.round(n(a,0) + (n(b,0) - n(a,0)) * t),
        g = Math.round(n(a,1) + (n(b,1) - n(a,1)) * t),
        z = Math.round(n(a,2) + (n(b,2) - n(a,2)) * t);
    return "#" + [r,g,z].map(function(v){ return ("0"+v.toString(16)).slice(-2); }).join("");
  }
  function escapar(s){
    return String(s == null ? "" : s).replace(/[&<>"]/g, function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];
    });
  }
  /* Se conserva por compatibilidad: estas hojas son de uso clínico. */
  function modo(){ return "clinica"; }

  /* ---------- fichas ----------
     Pocas fichas, las más frecuentes, y un "+" para que la persona ponga la
     suya. Lo que agrega se guarda con la hoja y vuelve al recargar.        */
  var LIBRES = {};      // contenedorId -> [texto, ...]
  var REG = {};         // contenedorId -> {lista, alCambiar, sinMas}

  function unChip(contId, txt, id, alCambiar, libre){
    var b = crearEl("button", "chip" + (libre ? " libre" : ""));
    b.type = "button";
    b.id = id;
    b.setAttribute("data-txt", txt);
    b.appendChild(document.createTextNode(txt));
    if(libre){
      var x = crearEl("span", "quitarChip", "×");
      x.title = "Quitar";
      x.onclick = function(ev){
        ev.stopPropagation();
        var l = LIBRES[contId] || [], i = l.indexOf(txt);
        if(i >= 0) l.splice(i, 1);
        redibujar(contId);
        if(alCambiar) alCambiar();
        guardar();
      };
      b.appendChild(x);
    }
    b.onclick = function(){
      b.classList.toggle("activa");
      if(alCambiar) alCambiar();
      guardar();
    };
    return b;
  }

  function botonMas(contId, alCambiar){
    var mas = crearEl("button", "chip mas", "+");
    mas.type = "button";
    mas.title = "Agregar una tuya";
    mas.onclick = function(){
      var caja = mas.parentElement;
      var campo = document.createElement("input");
      campo.type = "text";
      campo.className = "chipNuevo";
      campo.placeholder = "En tus palabras…";
      caja.insertBefore(campo, mas);
      mas.style.display = "none";
      var cerrado = false;
      function cerrar(guardarlo){
        if(cerrado) return;
        cerrado = true;
        var txt = campo.value.trim();
        campo.remove();
        mas.style.display = "";
        if(guardarlo && txt){
          agregarLibre(contId, txt);
          if(alCambiar) alCambiar();
        }
      }
      campo.addEventListener("keydown", function(ev){
        if(ev.key === "Enter"){ ev.preventDefault(); cerrar(true); }
        if(ev.key === "Escape"){ ev.preventDefault(); cerrar(false); }
      });
      campo.addEventListener("blur", function(){ cerrar(true); });
      campo.focus();
    };
    return mas;
  }

  /* Agrega una ficha propia ya marcada. */
  function agregarLibre(contId, txt){
    if(!LIBRES[contId]) LIBRES[contId] = [];
    if(LIBRES[contId].indexOf(txt) < 0) LIBRES[contId].push(txt);
    redibujar(contId);
    var l = LIBRES[contId], id = contId + "-libre-" + l.indexOf(txt);
    if($(id)) $(id).classList.add("activa");
    guardar();
  }

  function redibujar(contId){
    var r = REG[contId];
    if(r) chips(contId, r.lista, r.alCambiar, r.sinMas);
  }

  /* chips("miCaja", ["Una","Otra"], alCambiar)  -> con boton "+"
     chips("miCaja", [...], alCambiar, true)     -> sin boton "+"          */
  function chips(contenedorId, lista, alCambiar, sinMas){
    var c = $(contenedorId);
    if(!c) return;
    REG[contenedorId] = {lista:lista, alCambiar:alCambiar, sinMas:sinMas};
    var marcadas = {};
    for(var k = 0; k < c.children.length; k++)
      if(c.children[k].classList.contains("activa"))
        marcadas[c.children[k].getAttribute("data-txt")] = 1;

    c.innerHTML = "";
    c.classList.add("chips");
    lista.forEach(function(txt, i){
      var b = unChip(contenedorId, txt, contenedorId + "-" + i, alCambiar);
      if(marcadas[txt]) b.classList.add("activa");
      c.appendChild(b);
    });
    (LIBRES[contenedorId] || []).forEach(function(txt, i){
      var b = unChip(contenedorId, txt, contenedorId + "-libre-" + i, alCambiar, true);
      if(marcadas[txt]) b.classList.add("activa");
      c.appendChild(b);
    });
    if(!sinMas) c.appendChild(botonMas(contenedorId, alCambiar));
  }

  /* Tarjetas con título y descripción. lista: [["Título","Descripción"], ...] */
  function opciones(contenedorId, lista, alCambiar, unica){
    var c = $(contenedorId);
    if(!c) return;
    c.innerHTML = "";
    c.classList.add("tarjetas");
    lista.forEach(function(par, i){
      var e = crearEl("div", "opcion");
      e.id = contenedorId + "-" + i;
      e.setAttribute("data-txt", par[0]);
      e.innerHTML = "<b>" + escapar(par[0]) + "</b><span>" + escapar(par[1] || "") + "</span>";
      e.onclick = function(){
        if(unica) for(var j=0;j<c.children.length;j++)
          if(c.children[j] !== e) c.children[j].classList.remove("activa");
        e.classList.toggle("activa");
        if(alCambiar) alCambiar();
        guardar();
      };
      c.appendChild(e);
    });
  }

  /* ---------- mostrador con ranuras ----------
     El patrón de arrastrar-o-tocar: un mostrador de piezas y unas ranuras que
     las reciben. Se arrastra en escritorio y se toca en celular.

     cfg = {bancoId, ranurasId, cupo, items:[{id,titulo,desc,grupo,color}],
            etiquetas:[...], alCambiar}                                     */
  function mostrador(cfg){
    var banco = $(cfg.bancoId), ranuras = $(cfg.ranurasId);
    var puestas = [];                       // ids colocados, en orden
    var porId = {};
    cfg.items.forEach(function(it){ porId[it.id] = it; });

    function pintarBanco(){
      var grupos = [], vistos = {};
      cfg.items.forEach(function(it){
        var g = it.grupo || "";
        if(!vistos[g]){ vistos[g] = []; grupos.push(g); }
        vistos[g].push(it);
      });
      banco.innerHTML = "";
      banco.classList.add("mostrador");
      grupos.forEach(function(g){
        var caja = crearEl("div", "grupo");
        var col = vistos[g][0] && vistos[g][0].color;
        if(g){
          var tit = crearEl("div", "titulin", g);
          if(col) tit.style.color = col;
          caja.appendChild(tit);
        }
        var rejilla = crearEl("div", "tarjetas");
        vistos[g].forEach(function(it){
          var e = crearEl("div", "pieza" + (puestas.indexOf(it.id) >= 0 ? " usada" : ""));
          e.draggable = true;
          if(it.color){
            e.style.borderLeft = "4px solid " + it.color;
            e.style.background = it.color + "0f";
          }
          e.innerHTML = "<b>" + escapar(it.titulo) + "</b>" +
                        (it.desc ? "<span>" + escapar(it.desc) + "</span>" : "");
          e.addEventListener("dragstart", function(ev){
            ev.dataTransfer.setData("text/plain", it.id);
            e.classList.add("arrastrando");
          });
          e.addEventListener("dragend", function(){ e.classList.remove("arrastrando"); });
          e.addEventListener("click", function(){ poner(it.id); });
          rejilla.appendChild(e);
        });
        caja.appendChild(rejilla);
        banco.appendChild(caja);
      });
    }

    function pintarRanuras(){
      ranuras.innerHTML = "";
      ranuras.classList.add("ranuras");
      for(var i = 0; i < cfg.cupo; i++)(function(i){
        var id = puestas[i], it = id ? porId[id] : null;
        var r = crearEl("div", "ranura" + (it ? " llena" : ""));
        if(it && it.color){
          r.style.borderColor = it.color;
          r.style.background = it.color + "0f";
        }
        r.appendChild(crearEl("span", "orden", i + 1));
        if(it){
          if(it.color) r.lastChild.style.background = it.color + "26";
          var p = crearEl("div", "puesto");
          p.innerHTML = "<b>" + escapar(it.titulo) + "</b>" +
                        (it.desc ? "<span>" + escapar(it.desc) + "</span>" : "");
          r.appendChild(p);
          var x = crearEl("button", "sacar", "×");
          x.type = "button";
          x.title = "Sacar";
          x.onclick = function(){ sacar(i); };
          r.appendChild(x);
        } else {
          r.appendChild(crearEl("span", "hueco",
            (cfg.etiquetas && cfg.etiquetas[i]) || "Arrastra aquí, o toca una del mostrador"));
        }
        r.addEventListener("dragover", function(ev){
          ev.preventDefault();
          r.classList.add("encima");
        });
        r.addEventListener("dragleave", function(){ r.classList.remove("encima"); });
        r.addEventListener("drop", function(ev){
          ev.preventDefault();
          r.classList.remove("encima");
          poner(ev.dataTransfer.getData("text/plain"), i);
        });
        ranuras.appendChild(r);
      })(i);
    }

    function poner(id, i){
      if(!porId[id] || puestas.indexOf(id) >= 0) return;
      if(i === undefined || puestas.length < i){
        if(puestas.length >= cfg.cupo){ brindis("Las ranuras están llenas"); return; }
        puestas.push(id);
      } else {
        puestas[i] = id;
      }
      refrescar();
    }
    function sacar(i){
      puestas.splice(i, 1);
      refrescar();
    }
    function refrescar(){
      puestas = puestas.filter(function(x){ return x; });
      pintarBanco();
      pintarRanuras();
      if(cfg.alCambiar) cfg.alCambiar();
      guardar();
    }

    refrescar();
    return {
      elegidas: function(){ return puestas.map(function(id){ return porId[id]; }); },
      ids: function(){ return puestas.slice(); },
      cargar: function(lista){ puestas = (lista || []).filter(function(x){ return porId[x]; }); refrescar(); },
      poner: poner,
      refrescar: refrescar
    };
  }

  /* Devuelve los textos marcados dentro de un contenedor de chips u opciones */
  function activas(contenedorId){
    var c = $(contenedorId), fuera = [];
    if(!c) return fuera;
    for(var i=0;i<c.children.length;i++){
      var h = c.children[i];
      if(!h.classList.contains("activa")) continue;
      var t = h.getAttribute("data-txt");
      if(t == null) t = h.tagName === "DIV" ? h.querySelector("b").textContent : h.textContent;
      fuera.push(t);
    }
    return fuera;
  }
  /* Enlaza un input range con su etiqueta de valor */
  function medidor(idRango, idSalida, alCambiar){
    var r = $(idRango), s = $(idSalida);
    if(!r) return;
    function act(){
      if(s) s.textContent = r.value;
      if(alCambiar) alCambiar();
    }
    r.addEventListener("input", function(){ act(); guardar(); });
    act();
  }

  /* Gota que se llena según el nivel: 0 vacía, 10 rebosando. */
  function gota(nivel, tam){
    var n = Math.max(0, Math.min(10, nivel)) / 10;
    var t = tam || 26, uid = "g" + Math.random().toString(36).slice(2, 8);
    var col = mezcla("#c9b48a", "#2f8fbf", n);
    return '<svg class="gota" width="' + t + '" height="' + t * 1.18 + '" viewBox="0 0 24 28">' +
      '<clipPath id="' + uid + '"><path d="M12 1 C12 1 3 12 3 18 a9 9 0 0 0 18 0 C21 12 12 1 12 1 Z"/></clipPath>' +
      '<path d="M12 1 C12 1 3 12 3 18 a9 9 0 0 0 18 0 C21 12 12 1 12 1 Z" fill="#f2f5f8" ' +
      'stroke="' + col + '" stroke-width="1.6"/>' +
      '<rect x="0" y="' + (28 - 27 * n) + '" width="24" height="28" fill="' + col +
      '" clip-path="url(#' + uid + ')" opacity="0.9"/></svg>';
  }

  /* ---------- reloj de escena ----------
     Un solo latido para las hojas que se mueven. Llama a fn(dt) unas 25 veces
     por segundo mientras esté andando, con dt en segundos. Se para sola cuando
     la pestaña se va al fondo, para no gastar batería con una escena que nadie
     está mirando, y retoma sin saltos al volver.                            */
  function reloj(fn){
    var id = null, previo = 0, deuda = 0, PASO = 0.04, dormida = false;
    function latir(t){
      id = requestAnimationFrame(latir);
      if(!previo){ previo = t; return; }
      var dt = Math.min(.25, (t - previo) / 1000);
      previo = t;
      deuda += dt;
      if(deuda < PASO) return;
      fn(deuda);
      deuda = 0;
    }
    var r = {
      andar: function(){ if(!id){ previo = 0; deuda = 0; id = requestAnimationFrame(latir); } },
      parar: function(){ if(id){ cancelAnimationFrame(id); id = null; previo = 0; deuda = 0; } },
      anda:  function(){ return !!id; }
    };
    document.addEventListener("visibilitychange", function(){
      if(document.hidden && r.anda()){ dormida = true; r.parar(); }
      else if(!document.hidden && dormida){ dormida = false; r.andar(); }
    });
    return r;
  }

  /* ---------- persistencia ---------- */
  function camposGuardables(){
    var fuera = [], t = document.querySelectorAll("input,textarea,select");
    for(var i=0;i<t.length;i++) if(t[i].id) fuera.push(t[i]);
    return fuera;
  }
  function marcablesGuardables(){
    var fuera = [], t = document.querySelectorAll(".chip[id],.opcion[id]");
    for(var i=0;i<t.length;i++) fuera.push(t[i]);
    return fuera;
  }
  function guardar(avisar){
    if(!listo) return;
    var d = { _campos:{}, _marcas:{}, _libres: LIBRES };
    camposGuardables().forEach(function(e){
      d._campos[e.id] = (e.type === "checkbox" || e.type === "radio") ? e.checked : e.value;
    });
    marcablesGuardables().forEach(function(e){
      if(e.classList.contains("activa")) d._marcas[e.id] = 1;
    });
    if(ganchos.extra) d._extra = ganchos.extra();
    try{ localStorage.setItem(CLAVE, JSON.stringify(d)); }catch(e){}
    if(avisar) brindis("Guardado en este equipo");
  }
  function cargar(){
    var d = null;
    try{ d = JSON.parse(localStorage.getItem(CLAVE) || "null"); }catch(e){}
    if(!d) return false;
    if(d._extra && ganchos.restaurar) ganchos.restaurar(d._extra);
    LIBRES = d._libres || {};
    Object.keys(LIBRES).forEach(redibujar);
    camposGuardables().forEach(function(e){
      if(!(e.id in (d._campos||{}))) return;
      var v = d._campos[e.id];
      if(e.type === "checkbox" || e.type === "radio") e.checked = !!v; else e.value = v;
    });
    marcablesGuardables().forEach(function(e){
      if((d._marcas||{})[e.id]) e.classList.add("activa");
    });
    return true;
  }
  function limpiar(){
    if(!confirm("¿Empezar de nuevo? Se borrará lo que está en pantalla en este equipo.")) return;
    try{ localStorage.removeItem(CLAVE); }catch(e){}
    location.reload();
  }

  /* ---------- copiar resumen para la historia clínica ---------- */
  function encabezadoResumen(){
    var l = [], t = document.querySelector("h1");
    l.push((t ? t.textContent : "Herramienta").toUpperCase());
    var pares = [["nombre","Consultante"],["fecha","Fecha"],["sesion","Sesión"],
                 ["profesional","Profesional"]];
    pares.forEach(function(p){
      var e = $(p[0]);
      if(e && e.value.trim()) l.push(p[1] + ": " + e.value.trim());
    });
    return l.join("\n");
  }
  function notasProResumen(){
    var l = [], pares = [["proObservaciones","Observaciones"],["proHipotesis","Hipótesis de trabajo"],
                         ["proTarea","Tarea acordada"],["proProxima","Para la próxima sesión"]];
    pares.forEach(function(p){
      var e = $(p[0]);
      if(e && e.value.trim()) l.push(p[1].toUpperCase() + "\n" + e.value.trim());
    });
    return l.length ? "\n\n--- NOTAS DEL PROFESIONAL ---\n" + l.join("\n\n") : "";
  }
  function textoResumen(){
    var cuerpo = ganchos.resumen ? ganchos.resumen() : "";
    return encabezadoResumen() + "\n\n" + cuerpo + notasProResumen();
  }
  function copiar(){
    var txt = textoResumen();
    function viejo(){
      var a = document.createElement("textarea");
      a.value = txt;
      a.style.position = "fixed"; a.style.opacity = "0";
      document.body.appendChild(a); a.select();
      var ok = false;
      try{ ok = document.execCommand("copy"); }catch(e){}
      document.body.removeChild(a);
      brindis(ok ? "Resumen copiado al portapapeles" : "No se pudo copiar: revise el resumen impreso");
    }
    if(navigator.clipboard && window.isSecureContext){
      navigator.clipboard.writeText(txt).then(function(){
        brindis("Resumen copiado al portapapeles");
      }, viejo);
    } else viejo();
  }
  /* ---------- impresión ----------
     Los desplegables cerrados no salen en el papel. Antes de imprimir se
     abren, y al terminar vuelven a como estaban, para que la hoja impresa
     lleve lo que se trabajó aunque esté plegado en pantalla. */
  var abiertosAlImprimir = [];
  function antesDeImprimir(){
    abiertosAlImprimir = [];
    var ds = document.querySelectorAll("details");
    for(var i = 0; i < ds.length; i++){
      if(ds[i].classList.contains("catalogo")) continue;
      if(ds[i].classList.contains("borrar")) continue;
      if(!ds[i].open){ ds[i].open = true; abiertosAlImprimir.push(ds[i]); }
    }
  }
  function despuesDeImprimir(){
    abiertosAlImprimir.forEach(function(d){ d.open = false; });
    abiertosAlImprimir = [];
  }
  if(window.addEventListener){
    window.addEventListener("beforeprint", antesDeImprimir);
    window.addEventListener("afterprint", despuesDeImprimir);
    if(window.matchMedia){
      var mq = window.matchMedia("print");
      if(mq.addEventListener)
        mq.addEventListener("change", function(e){
          if(e.matches) antesDeImprimir(); else despuesDeImprimir();
        });
    }
  }

  function brindis(msg){
    var b = $("brindis");
    if(!b) return;
    b.textContent = msg;
    b.classList.add("visible");
    clearTimeout(b._t);
    b._t = setTimeout(function(){ b.classList.remove("visible"); }, 2200);
  }

  /* ---------- arranque ---------- */
  /* ---------- lámina: la letra grande solo cuando se proyecta ----------
     Las hojas expositivas ya no nacen en lámina. Se enciende con el botón de
     la barra y se recuerda en este equipo: en consulta uno a uno la letra
     grande alargaba la hoja sin aportar nada. */
  function lamina(encender){
    var b = document.body;
    if(!b.hasAttribute("data-laminable")) return;
    var on = encender === undefined ? !b.classList.contains("lamina") : !!encender;
    b.classList.toggle("lamina", on);
    var bt = document.querySelector(".botonLamina");
    if(bt) bt.textContent = on ? "Salir de lámina" : "Modo lámina";
    try{ localStorage.setItem(CLAVE + ":lamina", on ? "1" : "0"); }catch(e){}
  }
  function laminaGuardada(){
    if(!document.body.hasAttribute("data-laminable")) return;
    var v = null;
    try{ v = localStorage.getItem(CLAVE + ":lamina"); }catch(e){}
    lamina(v === "1");
  }

  /* ---------- un paso a la vez ----------
     Las hojas de cuatro y cinco pasos se leían enteras de un golpe y eso
     rompe la conducción de la sesión. Los pasos siguen en el documento —el
     motor de cada hoja los sigue encontrando— y solo se pliega lo que no se
     está trabajando. Al imprimir se abren todos. */
  function pasos(){
    /* Un paso es una sección numerada, venga como .paso o como .bloque: la
       tarjeta de crisis lleva dos de sus tres pasos como bloque. */
    var secs = [].slice.call(document.querySelectorAll("section.paso,section.bloque"))
                 .filter(function(s){ return s.querySelector("h2 .num"); });
    if(secs.length < 3) return;
    var arrancado = false;

    /* Hay hojas con pasos que aparecen y desaparecen según lo que se responda
       —las dos ramas de Verificar los hechos—: esas no cuentan mientras no
       estén a la vista. */
    function hay(k){ return k >= 0 && k < secs.length && !secs[k].hidden; }
    function siguiente(i){
      for(var k = i + 1; k < secs.length; k++) if(hay(k)) return k;
      return -1;
    }
    function abrir(i){
      if(i >= 0 && !hay(i)) i = siguiente(i);
      secs.forEach(function(s, k){
        s.classList.toggle("cerrado", k !== i);
        var nav = s.querySelector(":scope > .pasoNav");
        if(nav) nav.hidden = siguiente(k) < 0;
      });
      if(i > 0) secs[i].scrollIntoView({block:"start", behavior:"smooth"});
    }

    secs.forEach(function(s, i){
      var h = s.querySelector("h2");
      if(!h) return;
      s.classList.add("plegable");
      h.setAttribute("role", "button");
      h.setAttribute("tabindex", "0");
      h.addEventListener("click", function(ev){
        if(ev.target.closest("button,a,input,label")) return;
        abrir(s.classList.contains("cerrado") ? i : -1);
      });
      h.addEventListener("keydown", function(ev){
        if(ev.key === "Enter" || ev.key === " "){ ev.preventDefault(); h.click(); }
      });
      var nav = crearEl("div", "pasoNav");
      var b = crearEl("button", "", "Siguiente ›");
      b.type = "button";
      b.onclick = function(){ var k = siguiente(i); if(k >= 0) abrir(k); };
      nav.appendChild(b);
      s.appendChild(nav);

      /* Si la hoja destapa un paso, ese es el que toca: se abre solo. */
      new MutationObserver(function(){
        if(arrancado && !s.hidden && s.classList.contains("cerrado")) abrir(i);
      }).observe(s, {attributes:true, attributeFilter:["hidden"]});
    });

    abrir(0);
    setTimeout(function(){ arrancado = true; }, 0);
  }

  /* ---------- la ayuda, fuera del camino ----------
     El párrafo que explica para qué es el paso pasa detrás de un «?»: sigue
     ahí para quien lo necesite y deja de interponerse mientras se conduce.
     Solo los que cuelgan de la sección; los que acompañan a un campo dentro
     del cuerpo se quedan donde están. */
  function ayudas(){
    document.querySelectorAll("section.paso,section.bloque").forEach(function(s){
      var h = s.querySelector("h2");
      if(!h) return;
      var sueltas = [].slice.call(s.children).filter(function(e){
        return e.classList && e.classList.contains("ayuda");
      });
      if(!sueltas.length) return;
      var caja = crearEl("div", "ayudaCaja");
      caja.hidden = true;
      sueltas.forEach(function(x){ caja.appendChild(x); });
      s.insertBefore(caja, h.nextSibling);
      var b = crearEl("button", "comoAsi", "?");
      b.type = "button";
      b.title = "Para qué es este paso";
      b.setAttribute("aria-label", "Para qué es este paso");
      b.onclick = function(ev){
        ev.stopPropagation();
        caja.hidden = !caja.hidden;
        b.classList.toggle("abierto", !caja.hidden);
      };
      h.appendChild(b);
    });
  }

  /* Los tres arreglos de presentación, que no tocan el contenido de nadie. */
  function presentar(){
    ayudas();
    pasos();
    laminaGuardada();
  }

  function iniciar(cfg){
    CLAVE = cfg.clave || "herramienta";
    ganchos = cfg;

    var ni = $("proNoImprimir"), sincNotas = null;
    if(ni){
      sincNotas = function(){
        var s = document.querySelector("details.notas-pro");
        if(s) s.classList.toggle("borrar", ni.checked);
      };
      ni.addEventListener("change", sincNotas);
    }

    listo = true;
    cargar();
    if(sincNotas) sincNotas();
    if($("fecha") && !$("fecha").value)
      $("fecha").value = new Date().toLocaleDateString("es-CO");

    document.querySelectorAll("input,textarea,select").forEach(function(e){
      if(!e.id) return;
      e.addEventListener("input", function(){ guardar(); });
      e.addEventListener("change", function(){ guardar(); });
    });

    presentar();
    if(ganchos.alCambiar) ganchos.alCambiar();
  }

  /* ---------- arranque reducido ----------
     Para las hojas que ya traían su propio motor y su propia persistencia:
     cablea el botón de copiar y no toca nada más. */
  function soloModo(){
    var ni = $("proNoImprimir");
    if(ni) ni.addEventListener("change", function(){
      var s = document.querySelector("details.notas-pro");
      if(s) s.classList.toggle("borrar", ni.checked);
    });
    ganchos = { resumen: resumenGenerico };
    presentar();
  }

  /* Recorre las secciones y arma un texto con lo que esté diligenciado. */
  function resumenGenerico(){
    var fuera = [], secciones = document.querySelectorAll("section,header");
    for(var i = 0; i < secciones.length; i++){
      var s = secciones[i];
      if(s.classList.contains("notas-pro")) continue;
      var titulo = s.querySelector("h1,h2,h3");
      var lineas = [];
      var campos = s.querySelectorAll("input,textarea,select");
      for(var j = 0; j < campos.length; j++){
        var e = campos[j];
        if(e.type === "checkbox" || e.type === "radio" || !e.id) continue;
        if(!String(e.value).trim()) continue;
        var et = s.querySelector('label[for="' + e.id + '"]');
        lineas.push("  " + (et ? et.textContent.trim() + ": " : "") + e.value.trim());
      }
      var marcas = s.querySelectorAll(".activa,.llena,.activo,.on");
      var nombres = [];
      for(var k = 0; k < marcas.length; k++){
        var m = marcas[k];
        if(m.classList.contains("mini")) continue;   /* catálogo, no elección */
        var b = m.querySelector("b");
        var txt = (b ? b.textContent : m.textContent).replace(/\s+/g, " ").trim();
        if(txt && nombres.indexOf(txt) < 0) nombres.push(txt);
      }
      if(nombres.length) lineas.push("  Marcado: " + nombres.join(", "));
      if(lineas.length){
        if(titulo) fuera.push(titulo.textContent.trim().toUpperCase());
        fuera.push(lineas.join("\n"));
      }
    }
    return fuera.join("\n");
  }

  return {
    iniciar: iniciar, soloModo: soloModo, guardar: guardar, limpiar: limpiar, copiar: copiar,
    chips: chips, opciones: opciones, activas: activas, medidor: medidor,
    agregarLibre: agregarLibre, mostrador: mostrador, gota: gota,
    lamina: lamina,
    $: $, svg: svg, mezcla: mezcla, escapar: escapar, crearEl: crearEl,
    reloj: reloj,
    brindis: brindis, modo: modo, texto: textoResumen
  };
})();
