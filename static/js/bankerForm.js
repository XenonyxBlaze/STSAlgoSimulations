(function() {
    "use strict";

    const select = (el, all = false) => {
        el = el.trim()
        if (all) {
          return [...document.querySelectorAll(el)]
        } else {
          return document.querySelector(el)
        }
    }
    
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all)
        if (selectEl) {
          if (all) {
            selectEl.forEach(e => e.addEventListener(type, listener))
          } else {
            selectEl.addEventListener(type, listener)
          }
        }
    }

    on('change','#numProc',function() {
        let alloc = select('#allocMat');
        let calc = select('#calcMat');
        alloc.rows = this.value;
        calc.rows = this.value;
    })

    on('change','#man',function() {
        select('#calcMat').parentElement.children[0].innerText = "Enter " + this.value + " matrix";
    })
})()