import type { Product } from "../types/product";

export async function getProducts(): Promise<Product[]> {
  const response = await fetch("http://127.0.0.1:8000/api/catalog/products/");
  const result = await response.json();
  return result;
}
