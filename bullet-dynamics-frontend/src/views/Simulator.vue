<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <SimulatorConfigElement/>
  </div>
</template>

<script>
// @ is an alias to /src
import SimulatorConfigElement from '@/components/SimulatorConfigElement.vue'

export default {
  name: 'Simulator',
  components: {
    SimulatorConfigElement
  }
}
</script>
