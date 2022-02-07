db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Mulig lekkasje",
  Tags: ["FLFT1", "FLFT2"],
  Probability: NumberInt(98),
  Class: "Alarm",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: false,
  AcknowledgeBy: null,
  AcknowledgeComment: null,
});

db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Mulig lekkasje",
  Tags: ["FLFT2"],
  Probability: NumberInt(95),
  Class: "Alarm",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: false,
  AcknowledgeBy: null,
  AcknowledgeComment: null,
});

db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Mulig lekkasje",
  Tags: ["FLFT3"],
  Probability: NumberInt(97),
  Class: "Alarm",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: true,
  AcknowledgeBy: "56fc40f9d735c28df206d100",
  AcknowledgeComment: "Falsk alarm",
});

db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Kraftig endring i strømmning",
  Tags: ["FT1_121"],
  Probability: NumberInt(63),
  Class: "Warning",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: false,
  AcknowledgeBy: null,
  AcknowledgeComment: null,
});

db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Kraftig endring i strømmning",
  Tags: ["FT1_122"],
  Probability: NumberInt(55),
  Class: "Warning",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: false,
  AcknowledgeBy: null,
  AcknowledgeComment: null,
});

db.PeriodicReports.insertOne({
  CreatedBy: "test1@test.com",
  Created: ISODate("2019-02-12T00:00:00.000Z"),
  From: ISODate("2019-02-08T00:00:00.000Z"),
  To: ISODate("2019-02-12T00:00:00.000Z"),
  Description: "Kraftig endring i strømmning",
  Tags: ["FT1_130"],
  Probability: NumberInt(45),
  Class: "Warning",
  Customer: "56fc40f9d735c28df206d078",
  IsAcknowledge: true,
  AcknowledgeBy: "56fc40f9d735c28df206d100",
  AcknowledgeComment: "Feilen er utbedrett",
});
