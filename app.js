const app = Vue.createApp({
    // data, functions etc
    // template: '<h2>I am the template</h2>',
    data() {
      return {
        color: 'yellow',
        size: 18,
        showThemes: false,
        isHighlighted: false
      }
    },
    methods: {
        toggleThemes(){
            this.showThemes = !this.showThemes
        },
        toOffWhite(){
            this.color = 'yellow'
        },
        toBlackWhite(){
            this.color = 'blue'
        },
        changeFontSize(size){
            console.log(size)
            this.size = size
        },
        highlight(){
            this.isHighlighted = !this.isHighlighted
        }
    }
  })
  
  app.mount('#app')