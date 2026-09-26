import { getProducts } from "../../lib/api";

export default async function ShopPage() {
  const products = await getProducts();

  return (
    <div>
      <h1>Shop</h1>

      {products.map((product) => (
        <div key={product.id}>
          <h2>{product.name}</h2>

          <p>Category: {product.category_name}</p>

          <p>Price: {product.base_price} SAR</p>
        </div>
      ))}
    </div>
  );
}
