import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

/* Data */
const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 0 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 15 }
]

/* Data Access */

function getItemById(id) {
    return listProducts.filter((items) => items.itemId === id);
}

/* Express Server */
const app = express();
const port = 1245;

const notFound = { status: 'Product not found' };

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

/* Products */
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

/* Product detail */
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json(notFound);
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const stock = currentStock !== null ? currentStock : item.initialAvailableQuantity;

  item.currentQuantity = stock;
  res.json(item);
});

/* Reserve a product */
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  const noStock = { status: 'Not enough stock available', itemId };
  const reservationConfirmed = { status: 'Reservation confirmed', itemId };

  if (!item) {
    res.json(notFound);
    return;
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) currentStock = item.initialAvailableQuantity;

  if (currentStock <= 0) {
    res.json(noStock);
    return;
  }

  reserveStockById(itemId, Number(currentStock) - 1);

  res.json(reservationConfirmed);
});

/* Redis */
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => console.log('Redis client connected to the server'));


const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  return await getAsync(`item.${itemId}`);
}