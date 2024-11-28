/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // remove
  collection.schema.removeField("9wh9dege")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "eud8gd47",
    "name": "participants",
    "type": "number",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "noDecimal": false
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "9wh9dege",
    "name": "participants",
    "type": "text",
    "required": true,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // remove
  collection.schema.removeField("eud8gd47")

  return dao.saveCollection(collection)
})
