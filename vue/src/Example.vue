<template>
  <div
    id="example"
  >
    Hello from Vue! The value you passed from Django was "{{ exampledjangovariable }}".
    <example-component :exampledjangovariable="exampledjangovariable" :exampleVueVariable="exampleVueVariable"></example-component>
  </div>
</template>

<script>
import ExampleComponent from './components/ExampleComponent.vue';



export default {
    name: 'Example',
    components: { ExampleComponent },
    data() {
      return {
        exampleVueVariable: "Vue is awesome for dynamic front ends!",
      }
    },
    props: {
        exampledjangovariable: {
            type: String,
            default() { return ''; },
        },
    },
};
</script>

<style>
</style>
