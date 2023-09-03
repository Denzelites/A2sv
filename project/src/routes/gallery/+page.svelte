<script lang='ts'>
    import 'iconify-icon'
    import { fade } from 'svelte/transition';
	import Generate from '../components/generate.svelte';
    import Hero_1 from './components/hero_1.svelte';

    let backtotop: any;
    let images: any = [
        {src:'images.jpeg', description:'stuff'},
        {src:'download.png', description:'stuff'},
        {src:'download (1).png', description:'stuff'},
        {src:'text2imgthumb.jpeg', description:'stuff'},
        {src:'onyi.jpg', description:'stuff'},
    ]
    
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: "smooth", // Optional: Add smooth scrolling animation
        });
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
<div transition:fade={{duration:300}} >
    <div class='wrapper row2'>
        <Hero_1 />
    </div>

    <div class="wrapper row3">
    <main class="hoc container clear"> 
        <!-- main body -->
        <!-- ################################################################################################ -->
        <div class="content"> 
        <!-- ################################################################################################ -->
        <div id="gallery">
            <figure>
            <header class="heading">Gallery nb: (to render all images once uploaded to nware)</header>
            <ul class="nospace clear">
                {#each images as img, i (i)}
                    {#if i % 4 == 0}
                        <li class="one_quarter first"><img src={img.src} alt={img.description}/></li>
                    {:else}
                        <li class="one_quarter"><img src={img.src} alt={img.description}/></li>
                    {/if}
                {/each}
            </ul>
            <!-- <figcaption>Gallery Description Goes Here</figcaption> -->
            </figure>
        </div>
        <!-- ################################################################################################ -->
        <!-- ################################################################################################ -->
        <!-- <nav class="pagination">
            <ul>
            <li><a href="#">&laquo; Previous</a></li>
            <li><a href="#">1</a></li>
            <li><a href="#">2</a></li>
            <li><strong>&hellip;</strong></li>
            <li><a href="#">6</a></li>
            <li class="current"><strong>7</strong></li>
            <li><a href="#">8</a></li>
            <li><a href="#">9</a></li>
            <li><strong>&hellip;</strong></li>
            <li><a href="#">14</a></li>
            <li><a href="#">15</a></li>
            <li><a href="#">Next &raquo;</a></li>
            </ul>
        </nav> -->
        <!-- ################################################################################################ -->
        </div>
    </main>
    </div>

    <section transition:fade={{duration: 300}}>
        <Generate />  
    </section>
</div>

<a on:keypress on:click={scrollToTop} bind:this={backtotop} 
id="backtotop" href="#top"><iconify-icon class='i' width="32" height="32" icon='simple-line-icons:arrow-up'></iconify-icon></a>

<style>
    section{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        /**color to be done later **/
    }
</style>