<template>
  <div class="home">
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
