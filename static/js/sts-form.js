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

    let inputs = select('input',true);
    inputs.forEach(input => {
        input.classList.add('mb-3','form-control');
    });

    let preempt = select('#preempt');
    let quantum = select('#quantum');
    let priority = select('#prior');
    
    on('change','#algo',function(){
        if(this.value == 'sjf' || this.value == 'prio'){
          preempt.disabled=false;
          preempt.value="0";
        }
        else{
          preempt.disabled=true;
          preempt.value="";
        }
        if(this.value == 'robin'){
            quantum.disabled=false;
            quantum.value="";
        }
        else{
            quantum.disabled=true;
            quantum.value="disabled";
        }
        if(this.value == 'prio'){
            priority.disabled=false;
            priority.value="";
        }
        else{
            priority.disabled=true;
            priority.value="disabled";
        }
    })

    let form = select('#STS');
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)

})()