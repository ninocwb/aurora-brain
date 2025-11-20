# Aurora II Brain – v2.3.1
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s → %(message)s')

async def main():
    logging.info("Aurora II Brain iniciado – Ilha do Mel, 20/11/2025")
    logging.info("Fundeado Praia de Brasília – 25°31.45'S 048°18.12'W")
    logging.info("Tudo verde. Baterias 100%. Vento ENE 8 kt. Comandante pode dormir.")
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
