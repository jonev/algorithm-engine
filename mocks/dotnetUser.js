db.createUser({
  user: "dotnet",
  pwd: "dotnet",
  roles: [
    {
      role: "readWrite",
      db: "AlgorithmConfigs",
    },
    {
      role: "readWrite",
      db: "Reports",
    },
  ],
});
