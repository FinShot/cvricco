import { createClient } from '@sanity/client'
import imageUrlBuilder from '@sanity/image-url'

export const client = createClient({
  projectId: 'iac24nk0',
  dataset: 'production',
  apiVersion: '2024-03-13',
  useCdn: true
})

const builder = imageUrlBuilder(client)

export const urlFor = (source: any) => {
  if (source?.asset?._ref?.includes('gif')) {
    return client.getDocument(source.asset._ref).then((asset: any) => asset.url)
  }
  return builder.image(source)
}