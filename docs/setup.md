# Setup Guide

> Warning: this is still very rough and needs to be expanded into a real setup guide.
> If you are familiar with web development and Cloudflare, you can probably get the site
> set up using this guide. If you are not familiar with those things, please wait until
> I can improve the documentation.

## Hosting

This guide is focused on creating a website that is hosted on Cloudflare R2 storage and
using the Cloudflare D1 sqlite-compatible database.

Since Hugo compiles a static website with HTML pages, you can host the site on any HTTP
server or hosting service. All you need to do is copy the files up to your public HTML
folder.

The download limit worker will only run on Cloudflare workers for now.

## Dependencies

- Hugo: https://gohugo.io/
- NodeJS: https://nodejs.org/en
- npm: included with NodeJS
- Cloudflare wrangler: https://developers.cloudflare.com/workers/wrangler/install-and-update/


## Site Setup

1. Sign up for Cloudflare
2. Issue a Privacy credit card number
3. Enable Cloudflare R2 storage
4. Create R2 storage buckets
  1. Site
  2. Downloads
5. Create Redirect Rules
  1. Redirect path to index
  2. Redirect HTTP to HTTPS
6. Rate Limiting Rules
  1. Security -> Bots -> Enable All
  2. Security -> WAF -> Rate Limiting
    1. if the path ends with `.safetensors`
    2. 5-10 requests in 10 seconds
    3. block
    4. for 10 seconds
7. Run Hugo build and deploy to site bucket
8. Upload tensors to downloads bucket

## Download Limit Setup

1. Create D1 database
  1. Apply schema
  2. Apply index
2. Create default token in the database
  1. Add the default token to the Hugo site config
3. Deploy a download worker
  1. Add the downloads domain to the worker
  2. Set the downloads domain in the Hugo config
4. Create R2 API key pair for download bucket
  1. Add key pair to R2 worker properties

