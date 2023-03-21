import { artifacts, ethers } from "hardhat";
import { abi } from "../artifacts/contracts/AnimalNFT.sol/Anie.json";

async function main() {
  const accounts = await ethers.getSigners();

  for (const account of accounts) {
    console.log(account.address);
  }

  const contract = new ethers.Contract(
    "0xB3B8dC504f53C896c94810Ab05DE91D6fB9E78b4",
    abi,
    accounts[0]
  );
  const tx = await contract.safeMint(
    "0xf81FC25d5cCa228B2AE0f8F72bCE5b368666c3B6",
    "ipfs://bafkreiczpkuvksofgpye2uv4o7pgfbcf7czgw4kvuls64yubh7wkuzfjva"
  );
  await tx.wait(1);
  console.log(`mint NFT: ${await contract.tokenURI(0)}`);

  // con？st tx = await contract.setApprovalForAll(
  //   "0x75fD65508B4Baf4b8df768857fa211Cf78299fFF",
  //   true
  // );
  // await tx.wait(1);
  // console.log(`transfer: ${tx.hash}`);

  // const tx = await contract["safeTransferFrom(address,address,uint256)"]("0xf81FC25d5cCa228B2AE0f8F72bCE5b368666c3B6", "0x706efd323f9873E86EFeAaD36Be79FFf2D58a329", 0)
  // await tx.wait(1)
  // console.log(`transfer: ${tx.hash}`)
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
