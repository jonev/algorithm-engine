db.AlgorithmConfig.insertOne({
  _id: ObjectId("56fc40f9d735c28df206d071"),
  Algorithm: "Algo1",
  RunIntervalMinutes: 1,
  DataPeriodeDays: 1,
  Customer: "TEST kunde",
  Tags: ["Tag1", "Tag2", "Tag3"],
  LastRun: ISODate("2000-01-01T00:00:00.000Z"),
});

db.AlgorithmConfig.insertOne({
  _id: ObjectId("56fc40f9d735c28df206d072"),
  Algorithm: "Algo2",
  RunIntervalMinutes: 2,
  DataPeriodeDays: 2,
  Customer: "TEST kunde",
  Tags: ["Tag1", "Tag2", "Tag3"],
  LastRun: ISODate("2000-01-01T00:00:00.000Z"),
});

db.AlgorithmConfig.insertOne({
  _id: ObjectId("56fc40f9d735c28df206d073"),
  Algorithm: "Algo3",
  RunIntervalMinutes: 3,
  DataPeriodeDays: 3,
  Customer: "TEST kunde",
  Tags: ["Tag1", "Tag2", "Tag3"],
  LastRun: ISODate("2000-01-01T00:00:00.000Z"),
});
