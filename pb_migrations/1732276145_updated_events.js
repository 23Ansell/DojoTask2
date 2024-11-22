/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "xdkusjpz",
    "name": "max_participants",
    "type": "number",
    "required": true,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "noDecimal": true
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("2tl1c81m6wlu7g2")

  // remove
  collection.schema.removeField("xdkusjpz")

  return dao.saveCollection(collection)
})
