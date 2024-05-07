import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// product data
const products = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// Redis setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.error(`Redis client error: ${error.message}`);
});
client.on('connect', () => {
  console.log('Redis client connected');
});

// Utility functions
const getProductById = (id) => products.find((product) => product.itemId === id);

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
};

// Express setup
const app = express();
const port = 1245;

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getProductById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId) ?? product.initialAvailableQuantity;
  product.currentQuantity = currentStock;

  res.json(product);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getProductById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null || currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, currentStock - 1);

  res.json({ status: 'Reservation confirmed', itemId });
});
