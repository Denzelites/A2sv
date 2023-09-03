<script>
    import '../layout/styles/layout.css'
    import '../layout/styles/app.css'
    import Navbar from './components/navbar.svelte';
    import Footer from './components/footer.svelte';

    export const prerender = true;
</script>

<body id='top'>
    <div class='bgded-overlay'>
        <div class=''>
            <Navbar />
        </div>
        
        <slot>
            
        </slot>

        <div class='wrapper row5'>
            <Footer />
        </div>
    </div>
</body>