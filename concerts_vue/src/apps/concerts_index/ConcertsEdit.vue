<template>
    <div>
    Load Songs <a :href=songs_link>Here</a>:
    <br>
    Load Concerts <a :href=concerts_link>Here</a>:
    <br>
    Create Artists <a :href=artists_link>Here</a>:
    </div>
    </template>
    <script>
    export default {
    name: 'App',
    components: {
    },
    data: function() {
    return {
        songs_link: ext_songs_link,
        concerts_link: ext_concerts_link,
        artists_link: ext_artists_link
    }},
    methods: {
    },
    }
    </script>