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
      else if (this.type == "ammunition") return "ammunition";
      else return "cannon";
    },
  },
  methods: {
    onDrop(event) {
      if (event.dataTransfer.getData("type") != this.type) return;

      const id = event.dataTransfer.getData("id");
      const payload = { configId: this.configId, id: id };

      if (this.type == "platform")
        this.$store.commit("updateConfigPlatform", payload);
      else if (this.type == "ammunition")
        this.$store.commit("updateConfigAmmunition", payload);
      else if (this.type == "cannon")
        this.$store.commit("updateConfigCannon", payload);
    },
    tooltip(component) {
      if (this.type == "platform") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      } else if (this.type == "ammunition") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$"
        );
      } else {
        return (
          component.desc +
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