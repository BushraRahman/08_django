<template>
    <div>
        This is the page where we are going to edit movie in vuejs, this is cool
        This is the form coming from django, displayed in vue
    </div>
    <div>
        <form method="post"><input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
        <p>
    <label for="id_name">Name:</label>
    <input type="text" name="name" maxlength="50" required="" id="id_name">
    
    
  </p>
<p>
    <label for="id_concerts">Concerts:</label>
    <select hidden name="concerts" required="" id="id_concerts" multiple="">
        <option v-for="concert in concerts" :value="concert.id" selected=""></option>
    </select>
    <multiselect v-model="concerts_selected" :options="concerts" :multiple="false" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the concert" label="name" track-by="name" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
        <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
    </multiselect>
</p>

<p>
    <label for="id_songs">Songs:</label>
    <select hidden name="songs" required="" id="id_songs" multiple="">
        <option v-for="song in songs" :value="song.id" selected=""></option>
    </select>
    <multiselect v-model="songs_selected" :options="songs" :multiple="false" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Choose the song" label="title" track-by="title" :preselect-first="true" style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
        <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single" v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
    </multiselect>
</p>
        <input type="submit" value="Save">
        </form>
    </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
export default {
  name: 'App',
  components: {
    Multiselect
  },
  data: function() {
  	return {
	    	csrf_token: ext_csrf_token,
	    	form: ext_form,
            name: null,
	    	submitting_form: false,
	    	form_error: [],
	    	form_updated: "",
            concerts: ext_concerts,
            concerts_selected: null,
            songs: ext_songs,
            songs_selected: null
	}},
    methods: {
        submit_form_fetch(){
        	this.form_error = []
        	this.form_updated = ""
        	let formData = new FormData();
        	let form_data = {
	            	'name': this.name,
	            	'concerts': this.concerts,
	            	'songs': this.songs,
        	}
        	for (var key in form_data) {
            		formData.append(key, form_data[key])
        	}
        	fetch(this.update_bis_url,
            	{
                	method: "post",
                	body: formData,
                	headers: {'X-CSRFToken': this.csrf_token},
                	credentials: 'same-origin'
            	}
        	).then(function(response) {
            	console.log('response', response)
            	return response.json()}).then(
	            	this.handleResponse).catch(
	                	(error) => {
	                	console.log('error', String(error))
	                	this.form_error=["error"]
    			})
    	},
    	handleResponse(response) {
        	console.log('json response', response)
        	if ('success' in response){
	            	if (response['success'] == true) {
	                	this.form_updated = "Artist has been created"
	            	} else {
	                	if ('errors' in response){
		                    	for (const [key, value] of Object.entries(response['errors'])) {
		                        	for (const error of value) {
		                            		this.form_error.push(`${key}: ${error}`)
		                        	}
	                    		}
	                	} else {
	                    		this.form_error=["Update failed - An error occurred but do not have more information about it"]
	                	}
	            	}
		} else {
	            	this.form_error=["Update failed - It has been an error on the form request"]
		}
    	}
    },
    computed: {
    }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>