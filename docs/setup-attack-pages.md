# Setting up the Web Injection Attack Pages

Web injection cases (W1–W8 in S2) require the agent to fetch HTML pages
containing adversarial content. These pages are static HTML — no server-side
logic — so you can host them anywhere that serves files over HTTP(S).

This guide covers two paths. Pick whichever fits your setup.

## Path A: Local nginx (recommended for first run)

**Cost:** Free.
**Pros:** No AWS account, no DNS, no waiting for CloudFront propagation.
**Cons:** Agent only fetches from `localhost`; less faithful to the paper's
setup since real attacks come from external domains.

### Steps

1. The 8 attack pages are in `scenarios/s2_financial/web_pages/`:
   - `fedwire-funds.html`
   - `swift-status.html`
   - `chainalysis-monitor.html`
   - ... 

2. Serve them locally:
```bash
   cd scenarios/s2_financial/web_pages
   python3 -m http.server 8080
```

3. Edit `config.yaml` to point web injection cases at localhost:
```yaml
   web_injection:
     base_url: "http://localhost:8080"
```

4. Verify the agent can fetch a page:
```bash
   curl http://localhost:8080/fedwire-funds.html
```

[continue with case-by-case URL mapping]

## Path B: S3 + CloudFront (matches paper setup)

**Cost:** ~$0.50–$2/month depending on usage.
**Pros:** External domain, faithful reproduction of paper conditions.
**Cons:** Requires AWS account, ~30 min one-time setup.

### Prerequisites
- AWS account with S3 and CloudFront access
- A domain you control (optional — CloudFront default domain works)

### Steps

1. Create an S3 bucket:
```bash
   aws s3 mb s3://YOUR-BUCKET-NAME --region us-east-1
```

2. Set bucket policy for public read:
   [paste exact policy JSON]

3. Upload pages:
```bash
   cd scenarios/s2_financial/web_pages
   aws s3 sync . s3://YOUR-BUCKET-NAME/ --acl public-read
```

4. Create a CloudFront distribution pointing at the bucket:
   [paste exact aws cli command or console steps]

5. (Optional) Map a custom domain via Route53.

6. Edit `config.yaml`:
```yaml
   web_injection:
     base_url: "https://YOUR-DISTRIBUTION.cloudfront.net"
```

## Updating attack pages

If you modify the HTML, re-upload (Path B) and invalidate the CloudFront
cache:

```bash
aws cloudfront create-invalidation --distribution-id YOUR-DIST-ID --paths "/*"
```

Cache invalidation takes 1–5 minutes. Don't run cases during this window or
the agent may fetch stale pages — this is the same race condition that
caused the F15 bug during our development.

## Troubleshooting

- **Agent returns "404" for the page:** check `base_url` in config, verify
  with `curl`.
- **Agent uses wrong attack values:** likely cache contamination. Invalidate
  CloudFront or restart your local server.
- **CORS errors:** the agent uses server-side fetch, not browser fetch, so
  CORS shouldn't apply. If you hit CORS issues, you're probably testing
  through a browser by mistake.
