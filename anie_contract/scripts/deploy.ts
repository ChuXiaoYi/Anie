import { ethers } from "hardhat";

async function main() {
  const Anie = await ethers.getContractFactory("Anie");
  const anie = await Anie.deploy();

  await anie.deployed();

  console.log(
    `contract deployed to ${anie.address}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
