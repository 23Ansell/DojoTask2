/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // update
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

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "zklcv19l",
    "name": "instructor_id",
    "type": "relation",
    "required": false,
    "presentable": true,
    "unique": false,
    "options": {
      "collectionId": "9qb6qieu30p9frb",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": null,
      "displayFields": null
    }
  }))

  return dao.saveCollection(collection)
})
