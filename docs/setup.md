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

### Site Dependencies

- Hugo: https://gohugo.io/

### Worker Dependencies

- NodeJS: https://nodejs.org/en
- npm: included with NodeJS
- Cloudflare wrangler: https://developers.cloudflare.com/workers/wrangler/install-and-update/

## Basic Site Setup

1. Sign up for Cloudflare
2. Issue a Privacy credit card number
3. Enable Cloudflare R2 storage
4. Create R2 storage buckets
    1. Site
    2. Downloads
5. Create Redirect Rules
    1. Redirect path to index
    2. Redirect HTTP to HTTPS
6. Run Hugo build
7. Upload site files from `public` folder to the site bucket
8. Upload tensors to the downloads bucket

## Adding Content

1. Create a subfolder in the `content/models` or `content/posts` folder for your new post
2. Copy the `template.md` file from `content/models` or `content/posts` into your new folder
3. Rename the file to `index.md`
4. Add images into the same post folder
5. Edit the `index.md` file to add your post content
6. When the post is ready, set the `draft` field to `false` and run `hugo build` again
7. Upload the site files to the site bucket again

## Download Limit Setup

I recommend setting up both the rate limiting rules and the download limit worker
to prevent abuse of the download links.

### Rate Limiting

1. Rate Limiting Rules
    1. Security -> Bots -> Enable All
    2. Security -> WAF -> Rate Limiting
        1. if the path ends with `.safetensors`
        2. 5-10 requests in 10 seconds
        3. block
        4. for 10 seconds

### Worker Setup

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
