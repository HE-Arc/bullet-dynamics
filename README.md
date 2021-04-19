# bullet-dynamics

Pour tester :
  - User : root
  - Password : toor
  

### Remarque concernat la sécurisation des routes api

Pour sécuriser les routes api il suffit d'ajouter la ligne suivate à chaque view Django que l'on souhaite sécuriser :
```permission_classes = (IsAuthenticated,)```
Et d'ajouter ce header à chaque requete axios sur une route api sécurisée:	
```headers: { Authorization:  `Bearer ${state.accessToken}` }```

#### Exemple d'une requete post sécurisée

##### Django
```
class  ConfigViewSet(viewsets.ModelViewSet):	
	permission_classes = (IsAuthenticated,)
	queryset = Config.objects.all()
	serializer_class = ConfigSerializer
```
##### Vue
```
await  getAPI.patch(
	`/api/users/${state.username}/`,
	 { "config":  myConfigs }, {
	headers: { Authorization:  `Bearer ${state.accessToken}` }
})
```
