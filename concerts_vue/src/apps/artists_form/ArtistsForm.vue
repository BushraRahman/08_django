<template>
    <div>
        This is the page where we are going to edit movie in vuejs, this is cool
        This is the form coming from django, displayed in vue
    </div>
    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Name:</label>
                <input type="text" name="name" value="Matrix" maxlength="100" required="" id="id_name">
            </p>    
            <button type="submit" class="btn btn-primary"
@click.prevent="submit_form_fetch"
:disabled="submitting_form">
Submit
</button>               
        </form>
    </div>
    <br><br>
With fetch this time
<br><br>
<div v-if="form_error">
	<ul>
		<li v-for="(error, index) in form_error">
			{{error}}
		</li>
	</ul>
</div>
<div v-if="form_updated">
	{{ form_updated }}
</div>
    
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data: function() {
  	return {
	    	csrf_token: ext_csrf_token,
	    	update_bis_url: ext_update_bis_url,
	    	form: ext_form,
            name: null,
            concerts: "joe mama",
            songs: "Heya",
	    	submitting_form: false,
	    	form_error: [],
	    	form_updated: "",
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