/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "jxfdtdehc0er9d3",
    "created": "2024-11-29 08:47:54.428Z",
    "updated": "2024-11-29 08:47:54.428Z",
    "name": "waiting_list",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "k6y5r2sp",
        "name": "user_id",
        "type": "relation",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "collectionId": "0dn0g8dyisc3gmx",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": null
        }
      },
      {
        "system": false,
        "id": "npm5mbil",
        "name": "event_id",
        "type": "relation",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "collectionId": "2tl1c81m6wlu7g2",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": null
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("jxfdtdehc0er9d3");

  return dao.deleteCollection(collection);
})
