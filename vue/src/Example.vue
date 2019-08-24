<template>
  <div
    id="example"
  >
    Hello from Vue! The value you passed from Django was "{{ exampledjangovariable }}".
    <example-component
      :exampledjangovariable="exampledjangovariable"
      :example-vue-variable="exampleVueVariable"
    />
  </div>
</template>

<script>
import ExampleComponent from './components/ExampleComponent.vue';


export default {
    name: 'Example',
    components: { ExampleComponent },
    props: {
        exampledjangovariable: {
            type: String,
            default() { return ''; },
        },
    },
    data() {
        return {
            exampleVueVariable: 'Vue is awesome for dynamic front ends!',
        };
    },
};
</script>

<style>
    #example {
        color: #111;
    }
</style>
