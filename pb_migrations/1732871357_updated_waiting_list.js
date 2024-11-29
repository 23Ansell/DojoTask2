/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("jxfdtdehc0er9d3")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "njsobemq",
    "name": "registration_date",
    "type": "date",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "dcsyprhj",
    "name": "status",
    "type": "text",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("jxfdtdehc0er9d3")

  // remove
  collection.schema.removeField("njsobemq")

  // remove
  collection.schema.removeField("dcsyprhj")

  return dao.saveCollection(collection)
})
