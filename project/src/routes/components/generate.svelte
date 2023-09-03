<script lang='ts'>
    import {SyncLoader} from 'svelte-loading-spinners'

    let prompt: string;
    let updating: boolean = false;
    let img: string = 'images.jpeg'
    const handleSubmit = async ()=>{
        updating = true
        const res = await fetch(
            'http://localhost:8000/generate-image', {
                'method':'POST',
                'headers':{
                    'Content-Type':'application/json'
                },
                'body':JSON.stringify({
                    prompt
                })
            }
        )
        const data = await res.json()
        if (data.status == 200){
            console.log(data)
            img = `data:image/png;base64,${data.image_data}`
        }
        updating = false
    }
</script>

<div class="text-[20px] flex justify-center w-[70%] p-[40px] bg-gradient-to-r from-[#123456] via-50% via-transparent
to-[#383030]">
    <div class="flex flex-col my-0 mx-auto justify-center min-w-[300px]">
        <!---heading-->
        <div class="flex flex-row items-center justify-center"><h2>Bring your imagination to life</h2></div>
        <!---prompt-->
        <div class="flex flex-col items-center justify-start">
            <input class='h-[30px] w-[100%] rounded-md p-[7px] text-black' bind:value={prompt}>
        </div>
        <!--buttons-->
        <div class="flex flex-col items-center justify-center">
            <button on:click={handleSubmit} id='generate' class='w-[40%] m-[7px] cursor-pointer bg-[#1f78d1] text-white align-bottom
            border-none rounded-xl hover:border '>Generate</button>
        </div>
    </div>
    <div class="flex flex-col my-0 mx-auto items-center justify-center min-w-[300px]">
        {#if !updating}
        <div class="m-auto max-w-fit max-h-fit rounded-sm text-left">
            <img class='object-cover w-full h-full' src={img} alt='something'/>
        </div>
        {:else if updating}
        <SyncLoader size="60" color="#FF3E00" unit="px" duration="1s"/>
        {/if}
    </div>
</div>

<style>

</style>