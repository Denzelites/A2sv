<script lang='ts'>
    import { fade } from "svelte/transition";
    import Generate from "../components/generate.svelte";
    let prompt: string;
    let img: string;
</script>

<section transition:fade={{duration: 300}}>
    <Generate />  
</section>

<style>
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    section{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        /**color to be done later **/
    }
</style>