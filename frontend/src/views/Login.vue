<template>
  <v-container class="grey lighten-5" fluid>
    <v-row justify="center">
      <h2 class="text-center">Please sign in</h2>
    </v-row>
    <v-row justify="center">
      <v-alert
        v-if="incorrectAuth"
        type="info"
        border="right"
        colored-border
        elevation="2"
        ><b>Login:</b> incorrect username or password - please try again</v-alert
      >
    </v-row>
    <v-row justify="center space-around">
      <v-form v-on:submit.prevent="login">
        <div class="form-group">
          <v-text-field
            type="text"
            name="username"
            id="user"
            v-model="username"
            class="form-control"
            placeholder="Username"
          />
        </div>
        <div class="form-group">
          <v-text-field
            type="password"
            name="password"
            id="pass"
            v-model="password"
            class="form-control"
            placeholder="Password"
          />
        </div>
        <v-btn block type="submit" class="btn btn-lg btn-primary btn-block"
          >Login</v-btn
        >
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      incorrectAuth: false,
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "Configuration" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>

<style>
body {
  background-color: #f4f4f4;
}
.login {
  background-color: #fff;
  margin-top: 10%;
}
input {
  padding: 25px 10px;
}
</style>