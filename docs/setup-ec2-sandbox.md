# Setting up the EC2 Sandbox

The agent runs inside an EC2 instance to provide an isolated environment
with filesystem, shell, and network access. This guide walks through
provisioning a sandbox from a fresh Ubuntu 24.04 AMI.

## Why a sandbox?

ClawSafety attacks include destructive actions (file deletion, config
modification). Running the agent on your local machine risks side effects.
The sandbox is ephemeral — created per evaluation run, destroyed after.

## Prerequisites

- AWS account with EC2 access
- vCPU quota of at least 16 in your region (default is usually higher)
- AWS CLI installed and configured (`aws configure`)
- An SSH key pair in your AWS region

## Cost estimate

- t3.medium: $0.0416/hour (~$0.05 per S2 case at 10-turn format)
- Full S2 run (24 cases × 3 trials × 1 model): ~$5–10
- Full benchmark across 5 models: ~$50–100

## Step 1: Choose region and instance type

Region: any. Paper used `us-east-1`. Stick with one region per run to keep
cleanup simple.

Instance type:
- `t3.medium` (2 vCPU, 4 GB RAM) — works for most S2 cases
- `t3.xlarge` (4 vCPU, 16 GB RAM) — needed if running parallel cases or
  using larger context windows

## Step 2: Launch a fresh Ubuntu 24.04 instance

```bash
aws ec2 run-instances \
  --image-id ami-XXXXX \  # latest Ubuntu 24.04 in your region
  --instance-type t3.medium \
  --key-name YOUR-KEYPAIR \
  --security-group-ids sg-XXXXX \
  --subnet-id subnet-XXXXX
```

Get the latest Ubuntu 24.04 AMI ID:
```bash
aws ec2 describe-images \
  --owners 099720109477 \
  --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-noble-24.04-amd64-server-*" \
  --query "sort_by(Images, &CreationDate)[-1].ImageId" \
  --output text
```

## Step 3: Configure security group

Inbound: SSH (22) from your IP only. SSM doesn't need inbound rules.
Outbound: allow all (the agent fetches web pages, calls APIs).

## Step 4: Install dependencies

SSH in, then:

```bash
sudo apt update
sudo apt install -y python3.11 python3-pip git curl jq sqlite3
pip install --break-system-packages uv
```

[Continue with: install OpenClaw, install Nanobot, install NemoClaw, etc.
Each scaffold gets its own subsection with exact commands.]

## Step 5: Set up SSM access (optional, for the harness)

The harness uses SSM to push files and run commands. Without SSM you can
SCP files manually.

[SSM agent install + IAM role setup]

## Step 6: Verify

Run the smoke test:
```bash
python3 -c "import openclaw; print('ok')"
```

## Cleaning up

When done:
```bash
aws ec2 terminate-instances --instance-ids i-XXXXX
```

## Known issues

- `openshell sandbox upload` creates directories instead of files when the
  source path ends in a filename. Workaround: upload, then
  `cp /sandbox/file.py/file.py /sandbox/run.py`.
- OpenClaw session state persists across cases. The harness clears
  `/sandbox/.openclaw/agents/main/sessions/*` between cases — don't disable
  this.
- Default vCPU quota of 16 means max 8 concurrent t3.medium or 4 concurrent
  t3.xlarge instances.
