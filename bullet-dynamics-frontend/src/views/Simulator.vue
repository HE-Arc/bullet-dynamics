<template>
  <div class="home">
    <SimulatorConfigList/>
    <SimulatorConfigElement/>    
  </div>
</template>

<script>
// @ is an alias to /src
import SimulatorConfigElement from '@/components/SimulatorConfigElement.vue'
import SimulatorConfigList from '../components/SimulatorConfigList.vue'

export default {
  name: 'Simulator',
  components: {
    SimulatorConfigElement,
    SimulatorConfigList
  }
}
</script>
