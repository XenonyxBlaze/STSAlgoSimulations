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

    let hmList = select('.hm',true);
    hmList.forEach(e => {
        if (e.innerHTML == "H") {
            e.classList.add('bg-success','bg-opacity-25','border','border-success');
        } else if (e.innerHTML == "M") {
            e.classList.add('bg-danger','bg-opacity-25','border','border-danger');
        }
    });

    let relocLis = select('#reloc').children;
    let x = relocLis.length;

    for(let i = 0; i < x; i++) {
        let relocLi = relocLis[i];
        let relocLiChildren = relocLi.children;
        let y = relocLiChildren.length;
        if (relocLiChildren[1].innerHTML=="M"){
            relocLiChildren[y-1].classList.remove('bg-warning','border-warning');
            relocLiChildren[y-1].classList.add('bg-info','border-info');
        }
    }


})()