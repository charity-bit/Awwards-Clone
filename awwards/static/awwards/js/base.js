
    searchForm = document.querySelector('.search-form')
    submit = document.querySelector('.submit')
    logo = document.querySelector('.logo')
    profile = document.querySelector('.profile')
    searchBtn = document.querySelector('.search')
    close = document.querySelector('.close')
    searchBtn.addEventListener('click',function(e){
        console.log(e)
       
        submit.style.display = 'none'
        logo.style.display = 'none'
        profile.style.display = 'none'
        searchBtn.style.display = 'none'


        searchForm.style.display = 'flex'
        close.style.display = 'flex'
        

    })


    close.addEventListener('click',function(){
        submit.style.display = 'flex'
        logo.style.display = 'flex'
        profile.style.display = 'flex'
        searchBtn.style.display = 'flex'

        searchForm.style.display = 'none'
        close.style.display = 'none'
        
    })

    // .on('click',(e)=>{
    //    console.log(e)
    //   
    

