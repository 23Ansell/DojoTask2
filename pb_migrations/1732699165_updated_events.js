/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // remove
  collection.schema.removeField("zklcv19l")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "vkhwxrdu",
    "name": "assigned_instructor",
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
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "zklcv19l",
    "name": "instructor_id",
    "type": "relation",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "collectionId": "9qb6qieu30p9frb",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": null,
      "displayFields": null
    }
  }))

  // remove
  collection.schema.removeField("vkhwxrdu")

  return dao.saveCollection(collection)
})
