set -e

# 检查是否提供了 GPUS 参数
if [ -z "$1" ]; then
    echo "错误: 请提供 GPU 参数，例如: bash train.sh 0,1 ..."
    echo "用法: bash train.sh <GPUS> [其他参数...]"
    exit 1
fi

GPUS=$1
NB_COMMA=`echo ${GPUS} | tr -cd , | wc -c`
NB_GPUS=$((${NB_COMMA} + 1))
PORT=$((9000 + RANDOM % 1000))
EPOCHS=200

shift

echo "=========================================="
echo "启动训练实验"
echo "GPU设备: $GPUS"
echo "GPU数量: $NB_GPUS"
echo "主端口: $PORT"
echo "训练轮数: $EPOCHS"
echo "=========================================="

CUDA_VISIBLE_DEVICES=${GPUS} python -m torch.distributed.launch \
    --master_port ${PORT} \
    --nproc_per_node=${NB_GPUS} \
    main.py $@ \
    --epochs ${EPOCHS} \
    --base-epochs ${EPOCHS}