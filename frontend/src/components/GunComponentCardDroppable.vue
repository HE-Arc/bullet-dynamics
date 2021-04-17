<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on, attrs }">
      <v-card v-bind="attrs" v-on="on">
        <v-card-text style="padding: 0">
          <v-img
            :src="require('../assets/' + imgSrc + '_icon.png')"
            contain
            height="50"
            @drop="onDrop($event)"
            @dragover.prevent
            @dragenter.prevent
          />
        </v-card-text>
      </v-card>
    </template>
    <span v-if="component != null">
      {{ tooltip(component) }}
    </span>
    <span v-else> No configuration selected </span>
  </v-tooltip>
</template>


<script>
export default {
  name: "GunComponentCardDroppable",
  data() {
    return {};
  },
  computed: {
    imgSrc() {
      if (this.type == "platform") return "gun";
      else if (this.type == "ammo") return "ammo";
      else return "cannon";
    },
  },
  methods: {
    onDrop(event) {
      if (event.dataTransfer.getData("type") != this.type) return;

      const id = event.dataTransfer.getData("id");
      let patchedConfig = { "id": this.configId };

      if (this.type == "platform")
        patchedConfig["platform"] = id;
      else if (this.type == "ammo")
        patchedConfig["ammo"] = id;
      else if (this.type == "cannon")
        patchedConfig["cannon"] = id;
      
      this.$store.dispatch("patchConfig", patchedConfig);
    },
    tooltip(component) {
      if (this.type == "platform") {
        return (
          component.name +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      } else if (this.type == "ammo") {
        return (
          component.name +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$"
        );
      } else {
        return (
          component.name +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      }
    },
  },
  props: ["type", "configId", "component"],
};
</script>