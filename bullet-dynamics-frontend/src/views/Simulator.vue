<template>
  <div>
    <SimulatorConfigList/> 
    <SimulatorParamList/>  
  </div>
</template>

<script>
// @ is an alias to /src
import SimulatorConfigList from '../components/SimulatorConfigList.vue'
import SimulatorParamList from '../components/SimulatorParamList.vue'

export default {
  name: 'Simulator',
  components: {
    SimulatorConfigList,
    SimulatorParamList
  }
}
</script>
