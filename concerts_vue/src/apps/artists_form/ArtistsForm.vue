<template>
    <div>
        This is the form coming from django, displayed in vue
    </div>
    <div>
        <form method="post" class="form">
            <input type="hidden" name="csrfmiddlewaretoken"
                   v-bind:value="csrf_token">
            <p>
                <label for="id_name">Name:</label>
                <input type="text" name="name" v-model="name" maxlength="100" required="" id="id_name">
            </p>
            <button type="submit" class="btn btn-primary"
                @click.prevent="submit_form"
                :disabled="submitting_form">
                Submit
        </button>                  
        </form>
    </div>
    <br><br>
    
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
        name: null
    }},
    methods: {
        submit_form(){
            if (this.submitting_form === true) {
            return;
            }
            this.submitting_form = true
            var form = document.createElement('form');
            form.setAttribute('method', 'post');
            let form_data = {
                'csrfmiddlewaretoken': this.csrf_token,
                'name': this.name,
                'submitting_form': false
            }
            for (var key in form_data) {
                var html_field = document.createElement('input')
                html_field.setAttribute('type', 'hidden')
                html_field.setAttribute('name', key)
                html_field.setAttribute('value', form_data[key])
                form.appendChild(html_field)
            }
            document.body.appendChild(form);
            form.submit()
        },
    },
    computed: {
    }
}
</script>