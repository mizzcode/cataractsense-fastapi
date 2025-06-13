import asyncio
from app.db.database import init_db

async def main():
    await init_db()
    print("✅ Database dan tabel berhasil dibuat.")

if __name__ == "__main__":
    asyncio.run(main())
