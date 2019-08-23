<template>
  <div>Hello from the component!

    Django told me that "{{exampledjangovariable}}"

    Vue told me that "{{exampleVueVariable}}"
  </div>
</template>

<script>
export default {
    name: 'ExampleComponent',
    props: {
        exampledjangovariable: {
            type: String,
            default() { return ''; },
        },
        exampleVueVariable: {
            type: String,
            default() { return ''; },
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
