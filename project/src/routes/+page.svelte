<script lang='ts'>
	import Gallery from "./components/gallery.svelte";
    import Generate from "./components/generate.svelte";
    import Hero_1 from "./components/hero_1.svelte";
    import Hero_2 from './components/hero_2.svelte';
    import Hero_3 from "./components/hero_3.svelte";
    import About from "./components/about.svelte";
    import 'iconify-icon'

    import { fade } from "svelte/transition";

    let backtotop: any;
    
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: "smooth", // Optional: Add smooth scrolling animation
        });
    }

    function scrollIntoview({currentTarget}){
        const element = document.querySelector(currentTarget.getAttribute('href')) 

        if (!element){return}
        console.log(element)

        element.scrollIntoView({
            behavior: 'smooth'
        })
    }

    

    function checkScroll(){
        if(scrollY > 300){
            backtotop.classList.add("visible")
        } else{
            backtotop.classList.remove("visible")   
        }
    }
</script>
<svelte:window on:scroll={checkScroll}></svelte:window>

<section transition:fade={{duration:300}}>
    <div id="pageintro" class="hoc clear">
        <article> 
          <!-- ################################################################################################ -->
          <h3 class="heading">Explore the richness of African Literature and Arts</h3>
          <!-- <p>Discover the rich and vibrant African culture through the collection of our art pieces</p> -->
          <p class="font-x1 uppercase bold">Bring your imagination to life in the African style</p>
          <footer><a on:keypress on:click|preventDefault={scrollIntoview} class="btn" href="#prompt">Generate enthralling images</a></footer>
          <!-- ################################################################################################ -->
        </article>
    </div>
    
    <div class="wrapper row3">
        <Gallery />
    </div>
    
    <div class="wrapper bg-[#bcd8ee]">
        <Hero_1 />
    </div>
    
    <div class="wrapper row4">
        <Hero_2 />
    </div>
    
    <div class="wrapper row2" id='prompt'>
        <Hero_3 />
    </div>
    
    <div class='wrapper row4'>
        <About />
    </div>
    <!-- CTA -->
    
    <a on:keypress on:click|preventDefault={scrollIntoview} bind:this={backtotop} 
    id="backtotop" href='#top'><iconify-icon class='i' width="32" height="32" icon='simple-line-icons:arrow-up'></iconify-icon></a>    
</section>

<style>
    #pageintro{
      background: url('main.jpg');
    }
</style>