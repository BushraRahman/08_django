<template>
    <div>
        This is the page where we are going to edit movie in vuejs, this is cool
        This is the form coming from django, displayed in vue
    </div>
    <div>
        <form method="post"><input type="hidden" name="csrfmiddlewaretoken" value="YPeT7T9BwGSV6QZXfHrM9BK8RFSqvrjCKTq9T7J18qwsFbZMzJkKzMWxWSH22k32">
        <p>
    <label for="id_name">Name:</label>
    <input type="text" name="name" maxlength="50" required="" id="id_name">
    
    
  </p>

  
  <p>
    <label for="id_concerts">Concerts:</label>
    <select name="concerts" required="" id="id_concerts" multiple="">
  <option value="2">Follow</option>

  <option value="3">Ode To You</option>

  <option value="1">The Fifth World Tour</option>

</select>
    
    
  </p>

  
  <p>
    <label for="id_songs">Songs:</label>
    <select name="songs" required="" id="id_songs" multiple="">
  <option value="1">Song object (1)</option>

  <option value="4">Song object (4)</option>

  <option value="5">Song object (5)</option>

  <option value="6">Song object (6)</option>

</select>
    
    
      
    
  </p>
        <input type="submit" value="Save">
        </form>
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